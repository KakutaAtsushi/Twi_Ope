from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
from common.tweet import tweet_run
from common.oauth2 import get_oauth_token, get_access_token

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    oauth_url = get_oauth_token()
    if request.method == 'POST':
        tweet_run(request.form['tweet_body'])
    return render_template('index.html', oauth_url=oauth_url)


@app.route('/oauth', methods=['GET'])
def twitter_auth():
    oauth_token = request.args.get("oauth_token")
    oauth_verifier = request.args.get("oauth_verifier")
    screen_name = get_access_token(oauth_token, oauth_verifier)
    return render_template('index.html', screen_name=screen_name)


if __name__ == '__main__':
    app.run(debug=True)
