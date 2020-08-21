from flask import Flask

from .extensions import db, guard
from .models import User

def create_app():
    app = Flask(__name__)

    db.init_app(app)