from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from common.tweet import tweet_run
from common.oauth2 import get_oauth_token, get_access_token
from settings import DATABASE

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
app.config['USERNAME'] = 'user'
app.config['PASSWORD'] = 'pass'
# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE["HostURI"]
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_ECHO'] = True

# db = SQLAlchemy(app)


# @app.before_request
# def init():
#     db.create_all()


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/tweet', methods=['GET', 'POST'])
def tweet():
    oauth_url = get_oauth_token()
    if request.method == 'POST':
        tweet_run(request.form['tweet_body'])
    return render_template('tweet.html', oauth_url=oauth_url)


@app.route('/oauth', methods=['GET'])
def twitter_auth():
    oauth_token = request.args.get("oauth_token")
    oauth_verifier = request.args.get("oauth_verifier")
    screen_name = get_access_token(oauth_token, oauth_verifier)
    return render_template('tweet.html', screen_name=screen_name)  # renderテンプレート先は一考の余地あり


@app.route('/login', methods=["GET"])
def login_page():
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login_post():
    if 'login' not in session:
        session["login"] = False

    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        if app.config['USERNAME'] != username:
            flash("ユーザ名が異なります")
        elif password != app.config["PASSWORD"]:
            flash("パスワードが異なります")
        else:
            session["login"] = True
            session["username"] = username
        if session["login"]:
            return render_template('welcome.html')
        else:
            return redirect(url_for('login_page'))


@app.route('/sign_up_page', methods=['GET'])
def sign_up():
    return render_template('signup.html')


if __name__ == '__main__':
    app.run(debug=True)
