from flask import Flask

def create_app(environment_name='dev'):
    app = Flask(__name__)
    return app