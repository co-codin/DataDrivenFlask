import click
from flask.cli import with_appcontext

from .extensions import db
from .models import User, Question

