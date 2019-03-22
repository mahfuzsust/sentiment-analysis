from flask import Flask, render_template, request
from flask_cors import CORS
from flask.json import jsonify
import os 
from twitter_sentiment import TwitterSentiment

app = Flask(__name__, static_url_path='/static')
CORS(app)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/favicon.ico')
def favico():
    return app.send_static_file('favicon.ico')

@app.route('/sentiment', methods=["POST"])
def get_sentiment():
    data = request.json
    sen_analysis = TwitterSentiment()
    tweets = sen_analysis.get_sentimented_tweets(data["query"], data["count"])
    return jsonify(tweets)

if __name__ == '__main__':
    app.run()
    app.config.from_envvar('consumer_key')
