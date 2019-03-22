import tweepy
from tweepy import OAuthHandler
import os

class TwitterClient(object):
    def __init__(self):
        consumer_key = os.environ.get('consumer_key', None)
        consumer_secret = os.environ.get('consumer_secret', None)
        access_token = os.environ.get('access_token', None)
        access_token_secret = os.environ.get('access_token_secret', None)

        try:
            _auth = OAuthHandler(consumer_key, consumer_secret)
            _auth.set_access_token(access_token, access_token_secret)

            self._api = tweepy.API(_auth)
        
        except:
            print("Authentication failed")

    def get_tweets(self, query, count=10):
        try:
            return self._api.search(q = query, count = count)
        except tweepy.TweepError as e:
            print(e)



