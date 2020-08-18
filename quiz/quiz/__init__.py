from flask import Flask

from .extensions import db, login_manager
from .commands import create_tables
from .routes import main, auth

def create_app(config_file='settings.py'):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)

    db.init_app(app)

    login_manager.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(main)

    app.cli.add_command(create_tables)

    return app