import re
from textblob import TextBlob
from constants import POSITIVE, NEGATIVE, NEUTRAL

class SentimentAnalysis(object):
    def clean_text(self, text): 
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) |(\w+:\/\/\S+)", " ", text).split())
    
    def get_sentiment(self, text): 
        analysis = TextBlob(self.clean_text(text))
        if analysis.sentiment.polarity > 0: 
            return POSITIVE
        elif analysis.sentiment.polarity == 0: 
            return NEUTRAL
        else: 
            return NEGATIVE