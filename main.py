import hashlib

from flask import Flask, json, request, render_template, jsonify
from flask_login import LoginManager, login_user, logout_user, current_user
from flask_login.utils import login_required

from auth import check_login, hash_password
from model import User, getCursor

app = Flask(__name__)
app.config['SECRET_KEY'] = "sometimes i wonder about it"
login_manager = LoginManager()
login_manager.login_view = "/login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(username):
    s = getCursor()
    o = s.query(User).filter_by(username=username).first()
    return o

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        s = getCursor()
        user = s.query(User).filter_by(username=username).first()
        if user == None:
            return jsonify("Login failure")
        if user.password == hash_password(password):
            login_user(user)
            return "logged in"
    return jsonify("Login failure")

@app.route("/logout")
def logout():
    logout_user()
    return "Logged out"

@app.route("/signup")
def signup():
    return

@app.route("/dashboard")
@login_required
def dashboard():
    return "This is the dashboard. You are logged in as {}".format(current_user.username)

@app.route("/admin")
@login_required
def admin():
    return


if __name__ == '__main__':
    app.run(debug=True)
