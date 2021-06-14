from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return 'login'


@auth.route('/logout')
def logout():
    return 'logout'


@auth.route('sign-up')
def sign_up():
    return render_template('sign_up.html')