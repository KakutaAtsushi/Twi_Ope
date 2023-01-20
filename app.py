from flask import Flask, render_template, request, redirect, url_for, make_response, jsonify
from common.tweet import tweet_run

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        tweet_run(request.form['tweet_body'])
        return redirect(url_for('index'))
    return render_template('index.html')


@app.errorhandler(500)
def not_found(error):
    #エラーJSON作成
    result = {
        "error": error,
        "result":False
        }
    #エラーJSONを出力
    return make_response(jsonify(result), 500)


if __name__ == '__main__':
    app.run(debug=True)
