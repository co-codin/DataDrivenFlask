from flask import Blueprint
from yumroad.models import Product

products = Blueprint('products', __name__)

@products.route('/')
def index():
    products = Product.query.all()
    return products

@products.route('/<int:product_id>')
def details(product_id):
    product = Product.query.get_or_404(product_id)
    return product