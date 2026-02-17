# flaskit/generator.py
import os
from pathlib import Path

FOLDER_EMOJI = "📂"
FILE_EMOJI = "📝"
SKIPPED_EMOJI = "⚠️"

class Generator:
    def __init__(self, root: Path):
        self.root = root.resolve()
        self.generated_items = []

    def make_dirs(self, *dirs):
        for d in dirs:
            path = Path(d)
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)
                self.generated_items.append((FOLDER_EMOJI, f"[blue]{path}[/]"))
            else:
                self.generated_items.append((SKIPPED_EMOJI, f"[yellow]{path}[/]"))

    def write_file(self, path: Path, content: str):
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            self.generated_items.append((FILE_EMOJI, f"[magenta]{path}[/]"))
        else:
            self.generated_items.append((SKIPPED_EMOJI, f"[yellow]{path}[/]"))

    def generate_mvp(self):
        root = self.root
        self.make_dirs(
            root,
            root / "app",
            root / "app/templates",
            root / "app/static/css",
            root / "app/static/js",
            root / "app/static/images",
        )
        self.write_file(root / "main.py", "from app import app\n\nif __name__ == '__main__':\n    app.run(debug=True)\n")
        self.write_file(root / "app/__init__.py",
            "from flask import Flask\n\n"
            "app = Flask(__name__)\n"
            "app.config.from_mapping(\n"
            "    SECRET_KEY='dev',\n"
            ")\n\n"
            "from app import views  # noqa: E402, F401\n")
        self.write_file(root / "app/views.py",
            "from app import app\n"
            "from flask import render_template\n\n"
            "@app.route('/')\n"
            "def index():\n"
            "    return 'Hello Flask MVP!'\n")
        self.write_file(root / "app/auth.py",
            "# Simple auth placeholder\n"
            "def register_routes(app):\n"
            "    pass\n")
        self.write_file(root / "app/models.py", "# Models for MVP — add SQLAlchemy models here if needed.\n")
        self.write_file(root / "app/forms.py", "# WTForms for simple MVP forms (if needed)\n")
        self.write_file(root / "app/templates/layout.html",
            f"<!doctype html>\n"
            f"<title>{root.name}</title>\n"
            f"<body>\n"
            f"  <h1>Welcome to {root.name} (MVP)</h1>\n"
            f"  {{% block content %}}{{% endblock %}}\n"
            f"</body>\n")

    def generate_saas(self, db: str):
        root = self.root
        self.make_dirs(
            root,
            root / "app",
            root / "app/auth",
            root / "app/Feature1",
            root / "app/Feature2",
            root / "app/Feature3",
            root / "app/templates",
            root / "app/static",
            root / "app/tests",
        )
        # root files
        self.write_file(root / "run.py",
            "from app import create_app\n\n"
            "app = create_app()\n\n"
            "if __name__ == '__main__':\n"
            "    app.run(host='0.0.0.0', debug=True)\n")
        self.write_file(root / "config.py",
            "import os\n"
            "basedir = os.path.abspath(os.path.dirname(__file__))\n\n"
            "class BaseConfig:\n"
            "    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')\n"
            "    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))\n"
            "    SQLALCHEMY_TRACK_MODIFICATIONS = False\n")
        self.write_file(root / "requirements.txt", "Flask\nFlask_SQLAlchemy\n")
        self.write_file(root / "app/__init__.py",
            "from flask import Flask\n"
            "from .extensions import db\n\n"
            "def create_app(config_object='config.BaseConfig'):\n"
            "    app = Flask(__name__, instance_relative_config=False)\n"
            "    app.config.from_object(config_object)\n\n"
            "    # initialize extensions\n"
            "    db.init_app(app)\n\n"
            "    # register blueprints (auth + features)\n"
            "    from .auth import routes as auth_routes\n"
            "    app.register_blueprint(auth_routes.bp)\n\n"
            "    # feature blueprints (stubs)\n"
            "    try:\n"
            "        from .Feature1 import routes as f1_routes\n"
            "        app.register_blueprint(f1_routes.bp)\n"
            "    except Exception:\n"
            "        pass\n\n"
            "    try:\n"
            "        from .Feature2 import routes as f2_routes\n"
            "        app.register_blueprint(f2_routes.bp)\n"
            "    except Exception:\n"
            "        pass\n\n"
            "    try:\n"
            "        from .Feature3 import routes as f3_routes\n"
            "        app.register_blueprint(f3_routes.bp)\n"
            "    except Exception:\n"
            "        pass\n\n"
            "    return app\n")
        self.write_file(root / "app/extensions.py",
            "from flask_sqlalchemy import SQLAlchemy\n\n"
            "db = SQLAlchemy()\n")
        # auth blueprint files
        self.write_file(root / "app/auth/routes.py",
            "from flask import Blueprint, render_template\n\n"
            "bp = Blueprint('auth', __name__, url_prefix='/auth')\n\n"
            "@bp.route('/login')\n"
            "def login():\n"
            "    return 'Auth: login placeholder'\n")
        self.write_file(root / "app/auth/models.py",
            "from app.extensions import db\n\n"
            "# Add auth-related DB models here (User, Role, etc.)\n")
        self.write_file(root / "app/auth/forms.py",
            "# WTForms for auth forms\n")
        # Feature1, Feature2, Feature3 stubs
        for feature in ("Feature1", "Feature2", "Feature3"):
            self.write_file(root / f"app/{feature}/routes.py",
                f"from flask import Blueprint\n\n"
                f"bp = Blueprint('{feature.lower()}', __name__, url_prefix='/{feature.lower()}')\n\n"
                f"@bp.route('/')\n"
                f"def index():\n"
                f"    return '{feature} home'\n")
            self.write_file(root / f"app/{feature}/models.py",
                f"from app.extensions import db\n\n"
                f"# Models for {feature}\n")
            self.write_file(root / f"app/{feature}/services.py",
                f"# Business logic / services for {feature}\n")
        # tests placeholder
        self.write_file(root / "app/tests/test_app.py",
            "def test_placeholder():\n"
            "    assert True\n")
        # base template
        self.write_file(root / "app/templates/base.html",
            f"<!doctype html>\n"
            f"<title>{root.name}</title>\n"
            f"<body>\n"
            f"  <header><h1>{root.name} (SAAS)</h1></header>\n"
            f"  {{% block body %}}{{% endblock %}}\n"
            f"</body>\n")
