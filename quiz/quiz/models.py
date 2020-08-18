from .extensions import db

class User(db.Model):
    id = db.Coumn(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    password = db.Column(db.String(50))
    expert = db.Column(db.Boolean)
    admin = db.Column(db.Boolean)

    