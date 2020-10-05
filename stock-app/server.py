from flask import Flask
import requests

app = Flask(__name__)

def fetch_price(ticker):
    data = requests.get('https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'.format(ticker.upper()),
                        params={
                            'apikey': 'demo'
                        }).json()
    return data['price']

@app.route('/stock/<ticker>')
def stock(ticker):
    price = fetch_price(ticker)
    return 'The price of {ticker} is {price}'.format(ticker=ticker, price=price)