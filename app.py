from flask import Flask, render_template, request, redirect, url_for
from common.tweet import tweet_run

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/tweet', methods=['POST'])
def test():
    if request.method == 'POST':
        tweet_run(request.form['tweet_body'])
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
