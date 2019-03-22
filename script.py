from twitter_sentiment import TwitterSentiment
from constants import POSITIVE, NEGATIVE, NEUTRAL

sen_analysis = TwitterSentiment()
tweets = sen_analysis.get_sentimented_tweets("Donald Trump", 100)

# ptweets = [tweet for tweet in tweets if tweet['sentiment'] == POSITIVE]  
# print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets))) 
