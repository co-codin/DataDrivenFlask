import os
import sys
import flask
import data.db_session as db_session

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, folder)


app = flask.Flask(__name__)


def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)


def setup_db():
    db_session.global_init()


def register_blueprints():
    from sqlalchemy_intro.views import home_views
    from sqlalchemy_intro.views import package_views
    from sqlalchemy_intro.views import cms_views

    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


if __name__ == '__main__':
    main()
