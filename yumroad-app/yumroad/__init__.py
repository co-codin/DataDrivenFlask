from flask import Flask
from yumroad.config import configurations
from yumroad.extensions import db

def create_app(environment_name='dev'):
    app = Flask(__name__)
    app.config.from_object(configurations[environment_name])
    db.init_app(app)

    return app

# FLASK_ENV=development FLASK_APP="yumroad:create_app" flask run