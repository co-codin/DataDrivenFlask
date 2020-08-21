from flask import Flask
import os

from .extensions import db, guard
from .models import User

from .commands import create_users, create_database

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

    db.init_app(app)
    guard.init_app(app, User)

    app.cli.add_command(create_users)
    app.cli.add_command(create_database)

    return app