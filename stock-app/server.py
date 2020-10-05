from flask import Flask, render_template, redirect, url_for, request
from blueprints.stock import stock
from blueprints.home import home

app = Flask(__name__)

app.register_blueprint(stock)
app.register_blueprint(home)

@app.errorhandler(500)
def handle_error(execption):
    return render_template('500.html'), 500