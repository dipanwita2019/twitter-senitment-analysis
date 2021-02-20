"""Main module."""
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from textblob import TextBlob
from elasticsearch import Elasticsearch

# import twitter keys and tokens
from config import *

# create instance of elasticsearch
es = Elasticsearch()

consumer_key = "yours"
consumer_secret = "yours"
access_token = "yours"
access_token_secret = "yours"


# save the tweets into the elastic search
class TweetStreamListener(StreamListener):
    def on_status(self, status):
        # print(status.text)
        text = status.text
        blob = TextBlob(text)
        sent = blob.sentiment

        if sent.polarity < 0.0:
            sentiment = "negative"
        elif sent.polarity == 0.0:
            sentiment = "neutral"

        else:
            sentiment = "postive"

        # print(sentiment)

        # save in elastic search

        es.index(index="twitter-modi",
                 doc_type="practise02",
                 body={
                     "date": status.created_at,
                     "message": status.text,
                     "polarity": sent.polarity,
                     "sentiment": sentiment})

    def on_error(self, status_code):
        if status_code == 420:
            return False


if __name__ == '__main__':
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream_listener = TweetStreamListener()
    stream = Stream(auth=auth, listener=stream_listener, timeout=5)
    stream.filter(track=["modi", "narendra modi", "namo", "India", "india"])
