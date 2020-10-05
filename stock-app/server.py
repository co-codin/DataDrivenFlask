import requests
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

def fetch_price(ticker):
    data = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'.format(ticker.upper()),
                        params={'apikey': 'demo'}).json()
    return data["price"]

@app.route('/stocks/<string:ticker>')
def view_stock(ticker):
    stock_price = fetch_price(ticker)
    return render_template('stock_quote.html', ticker=ticker, stock_price=stock_price)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/lookup', methods=['POST'])
def lookup():
    return redirect(url_for('view_stock', ticker=request.form["ticker"]))

@app.route('/get_lookup', methods=['GET'])
def get_lookup():
    return redirect(url_for('view_stock', ticker=request.args["ticker"]))

