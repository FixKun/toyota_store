from flask import (
    Flask,
    current_app
)
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from flask_sqlalchemy import SQLAlchemy

login = LoginManager()
login.login_view = 'auth.login'

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(pages_bp)

    return app


from app.auth import bp as auth_bp
from app.pages import bp as pages_bp
