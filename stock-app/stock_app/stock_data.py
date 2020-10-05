import requests

def get_price(ticker):
    url = 'https://financialmodelingprep.com/api/v3/stock/real-time-price/{}'.format(ticker)
    return requests.get(url, params={
        'apikey': 'demo'
    }).json()["price"]

def get_financials(ticker):
    url = 'https://financialmodelingprep.com/api/v3/financials/income-statement/{}'.format(ticker)
    return requests.get(url, params={'period': 'quarter', 'apikey': 'demo'}).json()["financials"]

def eps_chart_url(financials):
    chart_data = [float(q["EPS"]) for q in financials]
    chart_params = {"type": 'line',
                    "data": {
                        'labels': [q["date"] for q in financials],
                        'datasets': [{'label': 'EPS', 'data': chart_data}]
                    }}
    return "https://quickchart.io/chart?width=500&height=200&c={}".format(chart_params)
