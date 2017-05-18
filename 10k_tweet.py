#Code to collect 10K Tweets
from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient

MONGO_HOST = 'mongodb://localhost/twitterdb'  # assuming you have mongoDB installed locally
# and a database called 'twitterdb'

WORDS = ['#trump']

CONSUMER_KEY = "b1rNDk0zgftNPMXyTwyK2NL2t"
CONSUMER_SECRET = "BMNmyoO5RnjC4Q8OkWl5fAEgImisWHQzN6jZYsUUxdwBnbz2M4"
ACCESS_TOKEN = "1031046644-MHJS0jz0Qulg8FRR6YIXZpTEKDTqqUVZZanfMBU"
ACCESS_TOKEN_SECRET = "MqIJZANGgZMhCcefqjOJTebxdno1zlTpdGzpY7ebzYtqY"


class StreamListener(tweepy.StreamListener):
    # This is a class provided by tweepy to access the Twitter Streaming API.

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        # This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            client = MongoClient(MONGO_HOST)

            # Use twitterdb database. If it doesn't exist, it will be created.
            db = client.twitterdb

            # Decode the JSON from Twitter
            datajson = json.loads(data)
            # grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']

            # insert the data into the mongoDB into a collection called twitter_search
            # if twitter_search doesn't exist, it will be created.
            if 'lang' in datajson and datajson['lang'] == 'en' and 'text' in datajson and 'trump' in datajson['text']:
                print("Tweet collected at " + str(created_at)+" #Trump")
                db.twitter_search.insert(datajson)
        except Exception as e:
            print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(WORDS))
streamer.filter(track = WORDS )
