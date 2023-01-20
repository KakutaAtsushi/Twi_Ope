from flask import Flask, render_template, request, redirect
from tweet import tweet_run

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/tweet', methods=['POST'])
def test():
    if request.method == 'POST':
        tweet_run(request.form['tweet_body'])
    return redirect('http://127.0.0.1:5000')


if __name__ == '__main__':
    app.run(debug=True)
