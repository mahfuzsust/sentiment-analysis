from twitter_client import TwitterClient
from sentiment_analysis import SentimentAnalysis
from constants import POSITIVE, NEGATIVE, NEUTRAL

class TwitterSentiment(object):
    def __init__(self):
        self.__api = TwitterClient()
        self.__sentiment = SentimentAnalysis()
    
    def get_sentimented_tweets(self, query, count = 10):
        fetched_tweets = self.__api.get_tweets(query = query, count = 200)
        tweets = []
        for tweet in fetched_tweets: 
            parsed_tweet = {}   
            parsed_tweet['text'] = tweet.text 
            parsed_tweet['sentiment'] = self.__sentiment.get_sentiment(tweet.text) 
            if tweet.retweet_count > 0: 
                if parsed_tweet not in tweets:
                    tweets.append(parsed_tweet) 
                else: 
                    tweets.append(parsed_tweet)
        return tweets
