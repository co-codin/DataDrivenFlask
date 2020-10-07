from sqlalchemy.orm import validates
from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash

from yumroad.extensions import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(), nullable=False)

    store = db.relationship("Store", uselist=False, back_populates='user')
    products = db.relationship("Product", back_populates='creator')

    @classmethod
    def create(cls, email, password):
        if not email or not password:
            raise ValueError('email and password are required')
        hashed_password = generate_password_hash(password)
        return User(email=email.lower().strip(), password=hashed_password)

    @property
    def is_authenticated(self):
        return not isinstance(self, AnonymousUserMixin)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price_cents = db.Column(db.Integer)
    picture_url = db.Column(db.Text)

    store = db.relationship("Store", uselist=False, back_populates="products")
    creator = db.relationship("User", uselist=False, back_populates="products")
    orders = db.relationship("Order", back_populates='product')

    @validates('name')
    def validate_name(self, key, name):
        if len(name.strip()) <= 3:
            raise ValueError('needs to have a name')
        return name

    @property
    def primary_image_url(self):
        return self.picture_url or "https://placehold.co/600x400?text={}".format(self.name)

class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    products = db.relationship("Product", back_populates='store', lazy='joined')
    user = db.relationship("User", uselist=False, back_populates="store")

    @validates('name')
    def validate_name(self, key, name):
        if len(name.strip()) <= 3:
            raise ValueError('needs to have a name')
        return name

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    purchaser_email = db.Column(db.String(255), nullable=False)
    purchased_at = db.Column(db.DateTime, nullable=False)
    payment_reference_id = db.Column(db.String(255))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    product = db.relationship("Product", back_populates="orders")
