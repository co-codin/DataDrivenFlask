from flask import Blueprint, render_template
import requests

stock = Blueprint('stock', __name__, url_prefix='/stock')

def fetch_price(ticker):
    data = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'.format(ticker.upper()),
                        params={'apikey': 'demo'}).json()
    return data["price"]

@stock.route('/<string:ticker>')
def view_stock(ticker):
    stock_price = fetch_price(ticker)
    return render_template('stock_quote.html', ticker=ticker, stock_price=stock_price)
