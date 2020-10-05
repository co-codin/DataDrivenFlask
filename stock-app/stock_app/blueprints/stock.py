from flask import Blueprint, render_template
from stock_app.stock_data import get_financials, get_price, eps_chart_url

stock = Blueprint('stock', __name__, url_prefix='/stocks')

@stock.route('/<string:ticker>/quote')
def view_stock(ticker):
    stock_price = get_price(ticker)
    return render_template('stock/stock_quote.html', ticker=ticker,
                           stock_price=stock_price)

@stock.route('/<string:ticker>/financials')
def financials(ticker):
    financial_data = get_financials(ticker)
    financial_data.sort(key=lambda quarter: quarter["date"])
    chart_url = eps_chart_url(financial_data)

    return render_template('stock/financials.html', ticker=ticker,
                           financials=financial_data, chart_url=chart_url)
