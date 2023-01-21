from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
from common.tweet import tweet_run
from common.oauth2 import oauth2

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    oauth_url = oauth2()
    if request.method == 'POST':
        tweet_run(request.form['tweet_body'])
    return render_template('index.html', oauth_url=oauth_url)


@app.route('/oauth/<string:oauth_token>', methods=['GET'])
def twitter_auth(oauth_token):

    return render_template('index.html',oauth_token=oauth_token)


if __name__ == '__main__':
    app.run(debug=True)
