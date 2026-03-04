from flask import Flask
from .config import Config
from .extensions import db, migrate
from .routes import tasks_bp
from .errors import register_error_handlers


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(tasks_bp, url_prefix='/api')
    register_error_handlers(app)

    return app
