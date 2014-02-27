from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import flash

from flask.ext.login import LoginManager
from flask.ext.login import UserMixin
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import logout_user
from flask.ext.login import confirm_login
from flask.ext.login import fresh_login_required

from flask.ext.bcrypt import check_password_hash

from app import app
from app.documents import Admin
from app.documents import Server

login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.refresh_view = 'reauth'
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(id):
    return User(id)

login_manager.setup_app(app)

class User(UserMixin):
    def __init__(self, username):
        self.name = username

@app.route('/login', methods=['GET', 'POST'])
def login():
    """  Log in user """

    if request.method == 'POST' and username in request.form:
        username = request.form.get('username')
        password = request.form.get('password')
        if authentication_check(username, password):
            if login_user(User(username)):
                flash("You have been logged in.")
                return redirect(url_for('/'))
            else:
                flash("You do not have sufficient access.")
        else:
            flash("Unable to log in.  Please verify your credentials.")
    return render_template('/login.html')


@app.route('/logout')
@login_required
def logout():
    """ Log out user """

    user_logout()
    flash("You have been logged out.")
    return redirect(url_for('/login'))

def authentication_check(username, password):
    """  Validate our user against ourrent db """
    if Admin.objects(username__exact=username):
        if Admin.objects(password__exact=check_password_hash(password)):
            return True
    return False

@app.route('/')
@login_required
def dashboard():
    return render_template('/dashboard.html')

@app.route('/add_server')
def add_server():
    
    
    server = Server(
      owner = current_user.get_id(),
      ip = payload.get('ip'),
      port = payload.get('port')
    )
